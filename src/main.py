from __future__ import annotations

from ctrs_system import CTRSSystem


def print_banner() -> None:
    print("=" * 64)
    print("CTRS CAPSTONE - Cat Triage and Rescue System")
    print("Author: Judilyn Lucena")
    print("=" * 64)


def main() -> None:
    system = CTRSSystem()
    print_banner()
    print(system.dashboard())

    print("\nAdoptable cats ordered by AVL tree (age, then ID):")
    for cat in system.list_adoptable_cats():
        print(
            f"- {cat.cat_id}: {cat.name} | {cat.age_months} months | "
            f"center={cat.center} | priority={cat.priority_score}"
        )

    print("\nHighest-priority foster request from heap:")
    request = system.next_foster_request()
    if request:
        print(
            f"- {request.foster_name} | urgency={request.urgency} | "
            f"capacity={request.capacity}"
        )

    print("\nMost urgent medical case from priority queue:")
    cat = system.next_medical_case()
    if cat:
        print(f"- {cat.cat_id}: {cat.name} | medical priority={cat.medical_priority}")

    print("\nHash-table lookup demo:")
    lookup = system.get_cat("C103")
    if lookup:
        print(f"- Found {lookup.cat_id}: {lookup.name} at {lookup.center}")

    print("\nWeighted graph / Dijkstra demo:")
    print(system.route_between("UFV Foster Hub", "Downtown Adoption Centre"))

    print("\nIntake stack history:")
    for entry in system.intake_history.to_list():
        print(f"- {entry}")


if __name__ == "__main__":
    main()
