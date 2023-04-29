from enum import Enum


class ItemType(Enum):
    Misc = 1
    ArchwingMod = 2
    PetCollar = 3
    Skin = 4
    MeleeRivenMod = 5
    WarframeMod = 6
    Prey = 7
    CompanionWeaponRivenMod = 8
    Fish = 9
    Node = 10
    Melee = 11
    Archwing = 12
    ConservationTag = 13
    Sentient = 14
    AyatanStar = 15
    FishPart = 16
    Plant = 17
    Syandana = 18
    Sigil = 19
    Medallion = 20
    ArchMeleeMod = 21
    KitgunComponent = 22
    PrimaryMod = 23
    FurColor = 24
    Predator = 25
    Rifle = 26
    Emotes = 27
    ParazonMod = 28
    RailjackMod = 29
    ArcadeMinigameUnlock = 30
    PistolRivenMod = 31
    CompanionMod = 32
    ArchGunRivenMod = 33
    Orbiter = 34
    ArchGunMod = 35
    PetParts = 36
    PetResource = 37
    Simulacrum = 38
    Glyph = 39
    ThemeSound = 40
    Gear = 41
    Neutral = 42
    Captura = 43
    Pistol = 44
    DualPistols = 45
    ShipSegment = 46
    Currency = 47
    Warframe = 48
    Pets = 49
    EidolonShard = 50
    ColorPalette = 51
    PlexusMod = 52
    ExaltedWeapon = 53
    Shotgun = 54
    Infestation = 55
    Tenno = 56
    ShipDecoration = 57
    KDriveComponent = 58
    ModSetMod = 59
    RifleRivenMod = 60
    Alloy = 61
    Resource = 62
    Orokin = 63
    ZawComponent = 64
    ArchMelee = 65
    Arcane = 66
    NotePacks = 67
    CutGem = 68
    FocusLens = 69
    SecondaryMod = 70
    TransmutationMod = 71
    ThemeBackground = 72
    NecramechMod = 73
    ArchGun = 74
    FishBait = 75
    Gem = 76
    Stalker = 77
    AyatanSculpture = 78
    ShotgunRivenMod = 79
    StanceMod = 80
    Extractor = 81
    MeleeMod = 82
    Corpus = 83
    CompanionWeapon = 84
    Themes = 85
    Specter = 86
    FocusWay = 87
    Grineer = 88
    Throwing = 89
    PeculiarMod = 90
    ZawRivenMod = 91
    Key = 92
    FurPattern = 93
    Amp = 94
    ShotgunMod = 95
    KDriveMod = 96
    Sentinel = 97
    KitgunRivenMod = 98
    Relic = 99
    ConservationPrey = 100


class Categories(Enum):
    Primary = 1
    Secondary = 2
    Melee = 3
    Misc = 4
    Arcanes = 5


class Item:
    def __init__(self) -> None:
        pass
