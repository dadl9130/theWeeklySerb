import { useState, useEffect } from "react";

export default function Header() {
  const [categories, setCategories] = useState<string[]>([]);

  useEffect(() => {
    fetch("http://localhost:8000/categories")
      .then(res => res.json())
      .then(data => setCategories(data.categories))
      .catch(err => console.error(err));
  }, []);

  return (
    <header className="flex justify-between p-4 border-b">
      <div>The Weekly Serb</div>
      <nav className="flex gap-4">
        {categories.map((cat) => (
          <div key={cat.slug}>{cat.name}</div>
        ))}
      </nav>
    </header>
  );
}
