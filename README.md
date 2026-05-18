# Polymorphism & Inheritance Practice — Animal Kingdom

## Overview

In this assignment you will model a small animal kingdom using **object-oriented programming**. You will practice two core OOP concepts:

- **Inheritance** — creating specialized classes that extend a shared base class
- **Polymorphism** — writing code that works with any animal through a common interface, letting each subclass define its own behavior

---

## Learning Objectives

By the end of this assignment you should be able to:

1. Define a base (parent) class with shared attributes and methods
2. Create subclasses that inherit from the base class
3. Override methods in subclasses to provide specialized behavior
4. Use a common interface to interact with different object types (polymorphism)
5. Understand when to use `super()` to call parent class logic

---

## File Structure

```
polymorphism_practice/
├── README.md
├── animals.py      ← Define your Animal base class and all subclasses here
└── main.py         ← Create animal objects and demonstrate polymorphism here
```

---

## Part 1 — The Base Class (animals.py)

Create an `Animal` base class with the following:

**Attributes (set in `__init__`):**
| Attribute | Type | Description |
|-----------|------|-------------|
| `name` | `str` | The animal's name |
| `age` | `int` | The animal's age in years |
| `sound` | `str` | The sound the animal makes |

**Methods:**
| Method | Description |
|--------|-------------|
| `speak()` | Prints `"<name> says <sound>"` |
| `move()` | Prints a generic movement message |
| `describe()` | Prints the animal's name, age, and type |
| `__str__()` | Returns a readable string representation |

---

## Part 2 — Subclasses (animals.py)

Create at least **four** animal subclasses that inherit from `Animal`. Each subclass must:

- Call `super().__init__(...)` in its constructor
- Override **at least one** method from the base class
- Add **at least one** attribute or method unique to that subclass

### Suggested Animals

| Class | Unique Attribute | Override |
|-------|-----------------|---------|
| `Dog` | `breed` | `speak()`, `move()` |
| `Bird` | `can_fly` (bool) | `move()` |
| `Fish` | `water_type` (`"fresh"` / `"salt"`) | `move()` |
| `Cat` | `indoor` (bool) | `speak()`, `move()` |

Feel free to swap in any animals you like!

---

## Part 3 — Demonstrating Polymorphism (main.py)

In `main.py`, do the following:

1. Import your classes from `animals.py`
2. Create at least **one instance of each subclass**
3. Store all animals in a **single list**
4. Loop over the list and call `speak()`, `move()`, and `describe()` on each animal — notice how each animal responds differently even though you call the same method names

### Example Output

```
Buddy says Woof!
Buddy runs on four legs.
Buddy is a 3-year-old Dog.

Tweety says Tweet!
Tweety flies through the air.
Tweety is a 1-year-old Bird.

...
```

---

## Part 4 — Stretch Goals

If you finish early, try one or more of the following:

- [ ] Add an **abstract base class** using Python's `abc` module so that `speak()` and `move()` *must* be overridden in every subclass
- [ ] Create a `Zoo` class that holds a list of animals and has methods like `feeding_time()` (calls `speak()` on all animals) and `exercise_time()` (calls `move()` on all animals)
- [ ] Add a `habitat` attribute and write a function that groups animals by habitat
- [ ] Override `__eq__` to compare two animals by name and age

---

## Grading Checklist

- [ ] `Animal` base class with all required attributes and methods
- [ ] At least four subclasses, each with a unique attribute and at least one override
- [ ] `super().__init__()` used correctly in every subclass
- [ ] `main.py` creates instances and demonstrates polymorphism with a loop
- [ ] Code is clean, readable, and free of errors
- [ ] (Bonus) Stretch goals attempted

---

## Tips

- Run your code often — catch errors early
- Use `isinstance(animal, Dog)` if you ever need to check the specific type, but try to rely on polymorphism instead
- If two subclasses share extra behavior, consider adding another layer of inheritance (e.g., a `Pet` class between `Animal` and `Dog`/`Cat`)
