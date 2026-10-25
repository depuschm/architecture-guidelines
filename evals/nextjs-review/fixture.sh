#!/usr/bin/env bash
# A tiny Next.js App Router app with planted problems: a Server Action without authorization,
# a secret behind NEXT_PUBLIC_, a whole database record passed to a Client Component,
# "use client" on the root layout, and plain <img> tags.
set -euo pipefail
mkdir -p app/profile app/components lib
cat > package.json <<'JSON'
{
  "name": "shop",
  "private": true,
  "scripts": { "dev": "next dev", "build": "next build" },
  "dependencies": { "next": "16.0.0", "react": "19.2.0", "react-dom": "19.2.0", "pg": "8.16.0" }
}
JSON
printf 'export default {};\n' > next.config.ts
cat > lib/db.ts <<'TS'
import { Pool } from 'pg';

export const db = new Pool({ connectionString: process.env.NEXT_PUBLIC_DATABASE_URL });

export async function getUser(id: string) {
  const { rows } = await db.query('SELECT * FROM users WHERE id = $1', [id]);
  return rows[0]; // id, email, password_hash, stripe_customer_id, is_admin, ...
}
TS
cat > app/actions.ts <<'TS'
'use server';
import { db } from '@/lib/db';

export async function deleteUser(id: string) {
  await db.query('DELETE FROM users WHERE id = $1', [id]);
}
TS
cat > app/layout.tsx <<'TSX'
'use client';
import { useState } from 'react';

export default function RootLayout({ children }: { children: React.ReactNode }) {
  const [menuOpen, setMenuOpen] = useState(false);
  return (
    <html lang="en">
      <body>
        <button onClick={() => setMenuOpen(!menuOpen)}>Menu</button>
        {menuOpen && <nav><a href="/profile">Profile</a></nav>}
        {children}
      </body>
    </html>
  );
}
TSX
cat > app/profile/page.tsx <<'TSX'
import { getUser } from '@/lib/db';
import ProfileCard from '../components/ProfileCard';

export default async function ProfilePage({ searchParams }: { searchParams: Promise<{ id: string }> }) {
  const { id } = await searchParams;
  const user = await getUser(id);
  return <ProfileCard user={user} />;
}
TSX
cat > app/components/ProfileCard.tsx <<'TSX'
'use client';
import { deleteUser } from '../actions';

export default function ProfileCard({ user }: { user: any }) {
  return (
    <div>
      <img src={user.avatar_url} />
      <h1>{user.email}</h1>
      <button onClick={() => deleteUser(user.id)}>Delete account</button>
    </div>
  );
}
TSX
