"use client";

import { useState } from "react";
import styles from "./page.module.css";

const scenarios = [
  { name: "Breezy", temperature: "16°", condition: "Cool air. A little coastal wind.", symbol: "≋", items: ["Cotton long sleeve", "Light windbreaker", "Everyday jeans", "Canvas sneakers"], reason: "A light outer layer takes the edge off the breeze without adding too much warmth." },
  { name: "Sunny", temperature: "24°", condition: "Clear skies. Keep things light.", symbol: "☼", items: ["Breathable tee", "No outer layer", "Linen trousers", "Canvas sneakers"], reason: "Lighter, breathable pieces make sense for this warmer example forecast." },
  { name: "Rainy", temperature: "12°", condition: "Grey skies. Showers on the way.", symbol: "☂", items: ["Merino long sleeve", "Waterproof shell", "Quick-dry trousers", "Water-resistant boots"], reason: "Rain protection and a warmer base layer help with this cool, wet example." },
];

const categories = ["Top", "Outerwear", "Bottom", "Footwear"];

export default function WeatherPreview() {
  const [selectedIndex, setSelectedIndex] = useState(0);
  const selected = scenarios[selectedIndex];

  return (
    <div className={styles.previewCard}>
      <div className={styles.cardTop}><span>SANTA CRUZ, CA</span><span className={styles.sampleBadge}>SAMPLE DATA</span></div>
      <div className={styles.scenarioButtons} role="group" aria-label="Example weather conditions">
        {scenarios.map((scenario, index) => (
          <button type="button" key={scenario.name} aria-pressed={selectedIndex === index} onClick={() => setSelectedIndex(index)}>
            {scenario.name}
          </button>
        ))}
      </div>
      <div aria-live="polite" aria-atomic="true">
        <div className={styles.weatherReading}>
          <div><span className={styles.temperature}>{selected.temperature}<small>C</small></span><p>{selected.condition}</p></div>
          <span className={styles.weatherSymbol} aria-hidden="true">{selected.symbol}</span>
        </div>
        <div className={styles.outfitHeading}><span>THE EXAMPLE OUTFIT</span><span>04 OUTFIT SLOTS</span></div>
        <ul className={styles.outfitList}>
          {selected.items.map((item, index) => (
            <li key={categories[index]}><span>{categories[index]}</span><strong>{item}</strong><span aria-hidden="true">↗</span></li>
          ))}
        </ul>
        <p className={styles.reason}><span aria-hidden="true">✳</span>{selected.reason}</p>
      </div>
    </div>
  );
}
