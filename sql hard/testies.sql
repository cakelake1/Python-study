SELECT 
    f.fortress_id,
    f.name,
    f.location,
    f.founded_year,
    JSON_OBJECT(
        'dwarf_ids', (
            SELECT JSON_ARRAYAGG(d.dwarf_id)
            FROM dwarves d
            WHERE d.fortress_id = f.fortress_id
        ),
        'resource_ids', (
            SELECT JSON_ARRAYAGG(fr.resource_id)
            FROM fortress_resources fr
            WHERE fr.fortress_id = f.fortress_id
        ),
        'workshop_ids', (
            SELECT JSON_ARRAYAGG(w.workshop_id)
            FROM workshops w
            WHERE w.fortress_id = f.fortress_id
        ),
        'squad_ids', (
            SELECT JSON_ARRAYAGG(s.squad_id)
            FROM military_squads s
            WHERE s.fortress_id = f.fortress_id
        )
    ) AS related_entities
FROM 
    fortresses f;
    [
  {
    "fortress_id": 1,
    "name": "Mountainhome",
    "location": "Eastern Mountains",
    "founded_year": 205,
    "related_entities": {
      "dwarf_ids": [101, 102, 103, 104, 105],
      "resource_ids": [201, 202, 203],
      "workshop_ids": [301, 302],
      "squad_ids": [401]
    }
  }
]
[
  {
    "workshop_id": 301,
    "name": "Royal Forge",
    "type": "Smithy",
    "quality": "Masterwork",
    "related_entities": {
      "craftsdwarf_ids": [101, 103],
      "project_ids": [701, 702, 703],
      "input_material_ids": [201, 204],
      "output_product_ids": [801, 802]
    }
  }
]
[
  {
    "squad_id": 401,
    "name": "The Axe Lords",
    "formation_type": "Melee",
    "leader_id": 102,
    "related_entities": {
      "member_ids": [102, 104, 105, 107, 110],
      "equipment_ids": [5004, 5005, 5006, 5007, 5008],
      "operation_ids": [601, 602],
      "training_schedule_ids": [901, 902],
      "battle_report_ids": [1101, 1102, 1103]
    }
  }
]