import Link from "next/link";
import { signOut } from "./auth/actions";
import styles from "./account-menu.module.css";

export default function AccountMenu({ email }: { email: string }) {
  const initial = email.charAt(0).toUpperCase() || "?";

  return (
    <details className={styles.menu}>
      <summary className={styles.trigger} aria-label="Account menu">
        <span className={styles.avatar} aria-hidden="true">{initial}</span>
        <span className={styles.chevron} aria-hidden="true">⌄</span>
      </summary>
      <div className={styles.panel}>
        <p className={styles.email}>{email}</p>
        <Link href="/dashboard">Dashboard</Link>
        <Link href="/wardrobe">Your wardrobe</Link>
        <Link href="/settings">Settings</Link>
        <form action={signOut}>
          <button type="submit">Sign out</button>
        </form>
      </div>
    </details>
  );
}
