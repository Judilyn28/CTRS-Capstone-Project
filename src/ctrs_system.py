from __future__ import annotations

from pathlib import Path
from typing import List

from avl_tree import AVLTree
from graph_routes import WeightedGraph
from hash_table import HashTable
from models import Cat, FosterRequest
from priority_queue import FosterPriorityQueue, MedicalPriorityQueue
from stack_history import Stack


class CTRSSystem:
    def __init__(self) -> None:
        self.cats = HashTable[str, Cat]()
        self.intake_history = Stack[str]()
        self.foster_queue = FosterPriorityQueue()
        self.medical_queue = MedicalPriorityQueue()
        self.adoption_tree = AVLTree()
        self.graph = WeightedGraph()
        graph_path = Path(__file__).resolve().parent.parent / "data" / "network.txt"
        self.graph.load_from_file(str(graph_path))
        self._seed_data()

    def _seed_data(self) -> None:
        sample_cats = [
            Cat("C101", "Milo", 8, 6, 9, "UFV Foster Hub", vaccines_due=True),
            Cat("C102", "Luna", 16, 8, 4, "Downtown Adoption Centre"),
            Cat("C103", "Pepper", 24, 4, 7, "Sardis Vet Partner", vaccines_due=True),
            Cat("C104", "Maple", 11, 9, 5, "Yarrow Intake Home"),
            Cat("C105", "Shadow", 30, 3, 10, "UFV Foster Hub"),
        ]
        for cat in sample_cats:
            self.register_cat(cat)

        for request in [
            FosterRequest("Alicia", 2, "Intermediate", "Beginner", 70),
            FosterRequest("Noah", 1, "Advanced", "Advanced", 92),
            FosterRequest("Priya", 3, "Beginner", "Intermediate", 60),
        ]:
            self.foster_queue.push(request)

    def register_cat(self, cat: Cat) -> None:
        self.cats.put(cat.cat_id, cat)
        self.intake_history.push(f"Intake recorded for {cat.cat_id} - {cat.name}")
        self.medical_queue.push(cat)
        if not cat.adopted:
            self.adoption_tree.insert((cat.age_months, cat.cat_id), cat)

    def get_cat(self, cat_id: str) -> Cat | None:
        return self.cats.get(cat_id)

    def list_all_cats(self) -> List[Cat]:
        return [cat for _, cat in self.cats.items()]

    def list_adoptable_cats(self) -> List[Cat]:
        return list(self.adoption_tree.inorder())

    def next_foster_request(self) -> FosterRequest | None:
        return self.foster_queue.pop()

    def next_medical_case(self) -> Cat | None:
        return self.medical_queue.pop()

    def route_between(self, start: str, end: str) -> str:
        result = self.graph.dijkstra(start, end)
        if not result.path:
            return f"No route found from {start} to {end}."
        path_str = " -> ".join(result.path)
        return f"Shortest rescue route: {path_str} ({result.distance:.1f} km)"

    def dashboard(self) -> str:
        all_cats = self.list_all_cats()
        vaccines_due = sum(1 for cat in all_cats if cat.vaccines_due)
        adopted = sum(1 for cat in all_cats if cat.adopted)
        return (
            "\nCTRS Dashboard\n"
            + "-" * 40
            + f"\nRegistered cats: {len(all_cats)}"
            + f"\nVaccines due: {vaccines_due}"
            + f"\nAdopted cats: {adopted}"
            + f"\nHash collisions observed: {self.cats.collisions}"
            + f"\nCurrent load factor: {self.cats.load_factor():.2f}"
            + f"\nFoster requests waiting: {len(self.foster_queue)}"
            + f"\nMost recent intake: {self.intake_history.peek()}"
        )
