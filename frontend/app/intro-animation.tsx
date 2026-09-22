import styles from "./intro-animation.module.css";

export default function IntroAnimation() {
  return (
    <div className={styles.intro} aria-hidden="true">
      <span className={styles.introMark}>-✳-</span>
      <span className={styles.introLabel}></span>
      <span className={styles.introLine} />
    </div>
  );
}
