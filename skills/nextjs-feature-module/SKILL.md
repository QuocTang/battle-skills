---
name: nextjs-feature-module
description: "When the user wants to create a new feature module in a Next.js App Router project following the standardized layered architecture (IO / Logic / UI separation). Use when user says 'create feature', 'add module', 'new tool', 'scaffold feature', or asks 'how to add a new page/feature' in a Next.js project."
tags: [nextjs, architecture, scaffold, react]
tools: [claude-code, cursor, gemini-cli]
version: 1.0.0
risk: low
date_added: "2026-03-01"
---

# Next.js Feature Module Generator

You are an expert Next.js architect. Your goal is to scaffold a **complete, production-ready feature module** following a strict layered architecture that separates IO, Business Logic, and UI concerns.

## When to Use This Skill

Use this skill when:

- User wants to create a new feature, page, or tool in a Next.js (App Router) project.
- User says "create feature", "add module", "new tool", "scaffold feature".
- User asks how to structure a new page with API integration in Next.js.

## Core Principles (MUST follow)

1. **Tách IO, Logic, UI** — Services chỉ IO (gọi API), Hooks chứa business logic, Components chỉ render.
2. **Không hardcode magic strings** — Sử dụng constants từ `config.ts` hoặc `core/app-storage/`.
3. **Feature module tự chứa** — Mỗi feature có types, config, hooks, components, index riêng.
4. **Public API qua index.ts** — Module khác chỉ import từ feature index, không import trực tiếp file con.

---

## Step 1: Create Folder Structure

Create the following directory structure inside `features/`:

```
features/<module-name>/
├── components/       # UI Components (chỉ render, không logic)
├── hooks/            # React Hooks & Business Logic
├── models/           # Data Models & View Models (DTO → Domain)
├── services/         # API Calls (IO Only — no logic, no transform)
├── types/            # Types & Interfaces
├── config.ts         # API endpoints & constants
├── query-keys.ts     # React Query Keys Factory (nếu cần, có thể gộp vào config.ts)
└── index.ts          # Public API (re-exports)
```

---

## Step 2: Create `config.ts`

Define API endpoints and React Query key factories.

```typescript
// features/<module-name>/config.ts

import { environment } from "@/core/environment";

export const <MODULE_NAME>_APIS = {
  query: `${environment.API_BASE_URL}/api/v1/<module-name>/list`,
  detail: `${environment.API_BASE_URL}/api/v1/<module-name>/detail`,
  create: `${environment.API_BASE_URL}/api/v1/<module-name>`,
  update: `${environment.API_BASE_URL}/api/v1/<module-name>`,
  delete: `${environment.API_BASE_URL}/api/v1/<module-name>`,
};

export const <MODULE_NAME>_QUERY_KEYS = {
  list: (filter: unknown) => ["<module-name>", "list", filter] as const,
  detail: (id: string) => ["<module-name>", "detail", id] as const,
};
```

> Replace `<module-name>` with the actual module slug (e.g. `user-management`).
> Replace `<MODULE_NAME>` with UPPER_SNAKE_CASE (e.g. `USER_MANAGEMENT`).

---

## Step 3: Create `types/index.ts`

Define all TypeScript interfaces and enums for this module. These represent the **raw API DTO shapes**.

```typescript
// features/<module-name>/types/index.ts

export interface <ModuleName>SearchCriteria {
  page: number;
  perPage: number;
  keyword?: string;
  // Add other filter fields here
}

export interface <ModuleName>Dto {
  id: string;
  name: string;
  created_at: string;
  // Add other raw API fields (snake_case from backend)
}
```

---

## Step 4: Create `services/<module-name>.service.ts`

**Rule: IO ONLY. No logic, no data transformation.**

The service layer is a thin wrapper around HTTP calls. It receives criteria/params, calls the API, and returns the **raw response data** unchanged.

```typescript
// features/<module-name>/services/<module-name>.service.ts

import { HttpClient } from "@/core/http/http-client";
import { <MODULE_NAME>_APIS } from "../config";
import type { <ModuleName>SearchCriteria } from "../types";

export const fetch<ModuleName>List = async (
  criteria: <ModuleName>SearchCriteria,
) => {
  const response = await HttpClient.get(<MODULE_NAME>_APIS.query, {
    params: criteria,
  });
  return response.data; // Return RAW data — no mapping!
};

export const fetch<ModuleName>Detail = async (id: string) => {
  const response = await HttpClient.get(`${<MODULE_NAME>_APIS.detail}/${id}`);
  return response.data;
};

export const create<ModuleName> = async (payload: Partial<<ModuleName>Dto>) => {
  const response = await HttpClient.post(<MODULE_NAME>_APIS.create, payload);
  return response.data;
};

export const update<ModuleName> = async (id: string, payload: Partial<<ModuleName>Dto>) => {
  const response = await HttpClient.put(`${<MODULE_NAME>_APIS.update}/${id}`, payload);
  return response.data;
};

export const delete<ModuleName> = async (id: string) => {
  const response = await HttpClient.delete(`${<MODULE_NAME>_APIS.delete}/${id}`);
  return response.data;
};
```

---

## Step 5: Create `models/index.ts`

**Rule: Transform raw API DTO → clean Domain Model.**

The model layer converts `snake_case` API responses into `camelCase` domain objects and performs any data normalization.

```typescript
// features/<module-name>/models/index.ts

import type { <ModuleName>Dto } from "../types";

export class <ModuleName>Model {
  id: string;
  name: string;
  createdAt: Date;

  constructor(data: <ModuleName>Dto) {
    this.id = data.id;
    this.name = data.name;
    this.createdAt = new Date(data.created_at);
  }

  // Static Factory Method — preferred entry point
  static fromAPI(data: unknown): <ModuleName>Model {
    const dto = data as <ModuleName>Dto;
    return new <ModuleName>Model(dto);
  }
}
```

---

## Step 6: Create Hooks

### 6a. `hooks/use-get-list.ts`

Use `useQuery` from TanStack React Query. **Map raw data through Model layer here.**

```typescript
// features/<module-name>/hooks/use-get-list.ts

import { useQuery } from "@tanstack/react-query";
import { fetch<ModuleName>List } from "../services/<module-name>.service";
import { <MODULE_NAME>_QUERY_KEYS } from "../config";
import { <ModuleName>Model } from "../models";
import type { <ModuleName>SearchCriteria } from "../types";

export const useGet<ModuleName>List = (criteria: <ModuleName>SearchCriteria) =>
  useQuery({
    queryKey: <MODULE_NAME>_QUERY_KEYS.list(criteria),
    queryFn: async () => {
      const response = await fetch<ModuleName>List(criteria);
      return {
        items: (response.list || []).map(<ModuleName>Model.fromAPI),
        total: response.total || 0,
      };
    },
  });
```

### 6b. `hooks/use-url-state.ts` (if the module has URL-based filters)

Manage filter/pagination state via URL search params for shareable and bookmarkable URLs.

```typescript
// features/<module-name>/hooks/use-url-state.ts

import { useSearchParams, useRouter, usePathname } from "next/navigation";
import { useMemo, useCallback } from "react";

export function use<ModuleName>UrlState() {
  const searchParams = useSearchParams();
  const router = useRouter();
  const pathname = usePathname();

  const criteria = useMemo(
    () => ({
      page: Number(searchParams.get("page")) || 1,
      perPage: Number(searchParams.get("perPage")) || 10,
      keyword: searchParams.get("keyword") || "",
    }),
    [searchParams],
  );

  const setCriteria = useCallback(
    (updates: Partial<typeof criteria>) => {
      const params = new URLSearchParams(searchParams);
      Object.entries(updates).forEach(([key, value]) => {
        if (value) params.set(key, String(value));
        else params.delete(key);
      });
      router.push(`${pathname}?${params.toString()}`);
    },
    [searchParams, router, pathname],
  );

  return { criteria, setCriteria };
}
```

---

## Step 7: Create `components/<ModuleName>List.tsx`

**Rule: Components only receive data & render. No API calls directly inside.**

```tsx
// features/<module-name>/components/<ModuleName>List.tsx

'use client';

import { useGet<ModuleName>List } from '../hooks/use-get-list';
import { use<ModuleName>UrlState } from '../hooks/use-url-state';

export function <ModuleName>List() {
  const { criteria, setCriteria } = use<ModuleName>UrlState();
  const { data, isLoading } = useGet<ModuleName>List(criteria);

  if (isLoading) return <div>Loading...</div>;

  return (
    <div>
      {/* Filter */}
      <input
        value={criteria.keyword}
        onChange={(e) => setCriteria({ keyword: e.target.value, page: 1 })}
        placeholder="Search..."
      />

      {/* List */}
      {data?.items.map((item) => (
        <div key={item.id}>{item.name}</div>
      ))}
    </div>
  );
}
```

---

## Step 8: Create `index.ts`

The public API barrel file. Other modules should ONLY import from this file.

```typescript
// features/<module-name>/index.ts

export * from "./components/<ModuleName>List";
export * from "./hooks/use-get-list";
export * from "./models";
export * from "./types";
```

---

## Step 9: Integrate with App Router

Create the Next.js page file under the `app/` directory.

```typescript
// app/(tools)/<module-name>/page.tsx

import { Metadata } from 'next';
import dynamic from 'next/dynamic';
import { ToolErrorBoundary } from '@/core/layout/content/ToolErrorBoundary';

const <ModuleName> = dynamic(() => import('@/features/<module-name>'), {
  loading: () => <div>Loading...</div>,
});

export const metadata: Metadata = {
  title: '<Module Display Name>',
  description: 'Mô tả module...',
};

export default function <ModuleName>Page() {
  return (
    <ToolErrorBoundary toolName="<Module Display Name>">
      <<ModuleName> />
    </ToolErrorBoundary>
  );
}
```

---

## Step 10: Register Storage Keys (if needed)

If the module uses `localStorage`, `sessionStorage`, or `cookies`, declare keys centrally:

```typescript
// core/app-storage/local-storage.ts

export const LOCAL_STORAGE_KEY = {
  GLOBAL: {
    THEME: "global.theme",
  },
  FEATURE: {
    // Add your module's keys here:
    // <MODULE_NAME>_DRAFT: "feature.<module-name>.draft",
  },
} as const;
```

### Storage Selection Guide

| Storage            | When to Use                            | Example                                |
| ------------------ | -------------------------------------- | -------------------------------------- |
| **localStorage**   | Persist across sessions, client-only   | Theme, user preferences, draft content |
| **sessionStorage** | Current tab only, lost on tab close    | Temp form state, scroll position       |
| **Cookie**         | Must be sent to server (SSR, API auth) | Auth token, locale (if needs SSR)      |

**Usage Pattern:**

```typescript
// ❌ WRONG — hardcoded key
localStorage.getItem("theme");

// ✅ CORRECT — use centralized key
import { LOCAL_STORAGE_KEY } from "@/core/app-storage/local-storage";
localStorage.getItem(LOCAL_STORAGE_KEY.GLOBAL.THEME);
```

---

## Step 11: Register Tool (if applicable to Universal Toolkit)

If the project follows the Universal Toolkit pattern with a Tool Registry, also register the new module:

1. Create `features/<module-name>/registry.ts`:

```typescript
import { lazy } from "react";
import { Wrench } from "lucide-react";
import type { ToolDefinition } from "@/core/registry/tool-registry.types";

const <ModuleName>Tool = lazy(() => import("./index"));

export const <moduleName>Registry: ToolDefinition = {
  id: "<module-name>",
  name: "<Module Display Name>",
  description: "Mô tả tool",
  icon: Wrench,
  category: "developer", // developer | design | converter | text | 3d
  tags: ["keyword1", "keyword2"],
  order: 10,
  path: "/<module-name>",
  component: <ModuleName>Tool,
};
```

2. Import in `config/tools.ts`:

```typescript
import { <moduleName>Registry } from "@/features/<module-name>/registry";

export const registeredTools: ToolDefinition[] = [
  // ... existing tools
  <moduleName>Registry, // ➕ Add here
];
```

---

## Layer Responsibility Cheat Sheet

| Layer         | File               | Rule                                                     |
| ------------- | ------------------ | -------------------------------------------------------- |
| **Service**   | `services/*.ts`    | IO only (API calls). Returns RAW data. No transform.     |
| **Model**     | `models/*.ts`      | Transform API DTO → Domain Model (snake → camel).        |
| **Hook**      | `hooks/*.ts`       | Business logic, `useQuery`/`useMutation`, maps via Model |
| **Component** | `components/*.tsx` | Receives data + renders UI. No direct API calls.         |

---

## Naming Conventions

| Item             | Convention                  | Example                      |
| ---------------- | --------------------------- | ---------------------------- |
| Feature folder   | `kebab-case`                | `user-management`            |
| Config constant  | `UPPER_SNAKE_CASE`          | `USER_MANAGEMENT_APIS`       |
| Type/Interface   | `PascalCase`                | `UserManagementDto`          |
| Model class      | `PascalCase + Model`        | `UserManagementModel`        |
| Hook             | `camelCase` + `use`         | `useGetUserManagementList`   |
| Component        | `PascalCase`                | `UserManagementList`         |
| Service function | `camelCase` + verb          | `fetchUserManagementList`    |
| Query key        | `UPPER_SNAKE + _QUERY_KEYS` | `USER_MANAGEMENT_QUERY_KEYS` |
