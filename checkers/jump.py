class Jump():
    id = 0
    parent_id = 0
    position = ()
    beated_pawn_id = 0

    def __init__(self, position: tuple, beated_pawn_id: int):
        self.position = position
        self.beated_pawn_id = beated_pawn_id

    def set_id(self, id:int):
        self.id = id

    def set_parent_id(self, parent_id: int):
        parent_id
