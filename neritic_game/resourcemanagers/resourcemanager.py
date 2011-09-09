''' Resource Wrappers '''

class Resource (object):
    def __init__ (self, filename):
        self.filename = filename
        self.loaded = True # using this bool seems like a recipe for failure
        self.data = None # data? really? that's a terrible name

    def load (self):
        ''' loads the resource into memory '''
        self.loaded = True        
    
    def unload (self):
        ''' unloads the resource from memory '''
        self.loaded = False
        self.data = None

class GraphicsResource (Resource):
    def load (self):
        super(GraphicsResource, self).load()
        self.data = sf.Image.load_from_file(self.filename)

''' Resource Manager(s)
    I can't really think of a reason to have more than one of these classes
    Please instance one for each set of resources (sounds, map graphics, entity graphics)
'''

class ResourceManager (object):
    def __init__ (self):
        self.resources = {}

    def add (self, resource_id, resource):
        ''' adds a resource to the manager's table '''
        self.resources[resource_id] = resource

    def get (self, resource_id):
        ''' returns a resource given an id, loads if necessary '''
        resource = None
        try:
            #FIXME: this is kind of stupid
            if not self.resources[resource_id].loaded:
                self.resources[resource_id].load()
            resource = self.resources[resource_id]
        except KeyError:
            print "No such resource {0}!".format(resource_id)
        except: 
            print "Could not laod resource {0}!".format(resource_id)

        return resource
