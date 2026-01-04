from enum import Enum


class MbdSymbol(str, Enum):
    """MBD symbol type"""  # noqa: E501

    NONE = "none"

    ARCLENGTH = "arclength"

    BETWEEN = "between"

    DEGREES = "degrees"

    PLUSMINUS = "plusminus"

    ANGULARITY = "angularity"

    CYLINDRICITY = "cylindricity"

    ROUNDNESS = "roundness"

    CONCENTRICITY = "concentricity"

    STRAIGHTNESS = "straightness"

    PARALLELISM = "parallelism"

    FLATNESS = "flatness"

    PROFILEOFLINE = "profileofline"

    SURFACEPROFILE = "surfaceprofile"

    SYMMETRY = "symmetry"

    PERPENDICULARITY = "perpendicularity"

    RUNOUT = "runout"

    TOTALRUNOUT = "totalrunout"

    POSITION = "position"

    CENTERLINE = "centerline"

    PARTINGLINE = "partingline"

    ISOENVELOPE = "isoenvelope"

    ISOENVELOPENONY145M = "isoenvelopenony145m"

    FREESTATE = "freestate"

    STATISTICALTOLERANCE = "statisticaltolerance"

    CONTINUOUSFEATURE = "continuousfeature"

    INDEPENDENCY = "independency"

    DEPTH = "depth"

    START = "start"

    LEASTCONDITION = "leastcondition"

    MAXCONDITION = "maxcondition"

    CONICALTAPER = "conicaltaper"

    PROJECTED = "projected"

    SLOPE = "slope"

    MICRO = "micro"

    TANGENTPLANE = "tangentplane"

    UNILATERAL = "unilateral"

    SQUAREFEATURE = "squarefeature"

    COUNTERSINK = "countersink"

    SPOTFACE = "spotface"

    TARGET = "target"

    DIAMETER = "diameter"

    RADIUS = "radius"

    SPHERICALRADIUS = "sphericalradius"

    SPHERICALDIAMETER = "sphericaldiameter"

    CONTROLLEDRADIUS = "controlledradius"

    BOXSTART = "boxstart"

    BOXBAR = "boxbar"

    BOXBARBETWEEN = "boxbarbetween"

    LETTERBACKWARDUNDERLINE = "letterbackwardunderline"

    PUNCTUATIONBACKWARDUNDERLINE = "punctuationbackwardunderline"

    MODIFIERBACKWARDUNDERLINE = "modifierbackwardunderline"

    NUMERICBACKWARDUNDERLINE = "numericbackwardunderline"

    BOXEND = "boxend"

    DATUMUP = "datumup"

    DATUMLEFT = "datumleft"

    DATUMRIGHT = "datumright"

    DATUMDOWN = "datumdown"

    DATUMTRIANGLE = "datumtriangle"

    HALFSPACE = "halfspace"

    QUARTERSPACE = "quarterspace"

    EIGHTHSPACE = "eighthspace"

    MODIFIERSPACE = "modifierspace"

    def __str__(self) -> str:
        return str(self.value)
