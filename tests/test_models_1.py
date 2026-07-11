from models.traveller_profile import TravellerProfile
from models.travel_dna import TravelDNA
from models.traveller_intent import TravellerIntent
from models.approval import ApprovalState


def main():

    profile = TravellerProfile()

    dna = TravelDNA()

    intent = TravellerIntent()

    approval = ApprovalState()

    print(profile)

    print(dna)

    print(intent)

    print(approval)

    print("\n✅ Milestone 1A Passed")


if __name__ == "__main__":
    main()
