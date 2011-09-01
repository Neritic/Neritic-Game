class World (object):
    ''' the game world state
        responsible for tracking entities, providing level information,
        and for loading and saving level data '''

    def __init__ (self):
        self.entities = []

    def load (self):
        #FIXME: implement generic load-from-file routine
        pass

    def save (self):
        #FIXME: implement generic save-to-file routine
        pass

    def update (self, t, dt):
        ''' central update function '''

        # things like weather or such could go here
        self.update_entities(t, dt)

    def update_entities (self, t, dt):
        for entity in self.entities:
            entity.update(t, dt)

    def add_entity (self, entity):
        ''' add an entity to the world '''
        
        # probably you'd do some checking or init code for the entity first here
        self.entities.append(entity)
