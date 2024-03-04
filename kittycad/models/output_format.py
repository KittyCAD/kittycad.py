import datetime
from typing import List, Optional, Dict, Union, Any, Literal
from uuid import UUID

from pydantic import BaseModel, Base64Bytes, AnyUrl, ConfigDict
from pydantic_extra_types.phone_numbers import PhoneNumber
from .base64data import Base64Data


from ..models.fbx_storage import FbxStorage



class fbx(BaseModel):
    """Autodesk Filmbox (FBX) format."""
    
    
    storage: FbxStorage
    
    
    
    type: Literal["fbx"] = "fbx"
    
    

    model_config = ConfigDict(
        protected_namespaces=()
    )
import datetime
from typing import List, Optional, Dict, Union, Any, Literal
from uuid import UUID

from pydantic import BaseModel, Base64Bytes, AnyUrl, ConfigDict
from pydantic_extra_types.phone_numbers import PhoneNumber
from .base64data import Base64Data


from ..models.gltf_presentation import GltfPresentation


from ..models.gltf_storage import GltfStorage



class gltf(BaseModel):
    """glTF 2.0. We refer to this as glTF since that is how our customers refer to it, although by default it will be in binary format and thus technically (glb). If you prefer ASCII output, you can set that option for the export."""
    
    
    presentation: GltfPresentation
    
    
    
    storage: GltfStorage
    
    
    
    type: Literal["gltf"] = "gltf"
    
    

    model_config = ConfigDict(
        protected_namespaces=()
    )
import datetime
from typing import List, Optional, Dict, Union, Any, Literal
from uuid import UUID

from pydantic import BaseModel, Base64Bytes, AnyUrl, ConfigDict
from pydantic_extra_types.phone_numbers import PhoneNumber
from .base64data import Base64Data


from ..models.system import System


from ..models.unit_length import UnitLength



class obj(BaseModel):
    """Wavefront OBJ format."""
    
    
    coords: System
    
    
    
    type: Literal["obj"] = "obj"
    
    
    
    units: UnitLength
    
    

    model_config = ConfigDict(
        protected_namespaces=()
    )
import datetime
from typing import List, Optional, Dict, Union, Any, Literal
from uuid import UUID

from pydantic import BaseModel, Base64Bytes, AnyUrl, ConfigDict
from pydantic_extra_types.phone_numbers import PhoneNumber
from .base64data import Base64Data


from ..models.system import System


from ..models.selection import Selection


from ..models.ply_storage import PlyStorage


from ..models.unit_length import UnitLength



class ply(BaseModel):
    """The PLY Polygon File Format."""
    
    
    coords: System
    
    
    
    selection: Selection
    
    
    
    storage: PlyStorage
    
    
    
    type: Literal["ply"] = "ply"
    
    
    
    units: UnitLength
    
    

    model_config = ConfigDict(
        protected_namespaces=()
    )
import datetime
from typing import List, Optional, Dict, Union, Any, Literal
from uuid import UUID

from pydantic import BaseModel, Base64Bytes, AnyUrl, ConfigDict
from pydantic_extra_types.phone_numbers import PhoneNumber
from .base64data import Base64Data


from ..models.system import System



class step(BaseModel):
    """ISO 10303-21 (STEP) format."""
    
    
    coords: System
    
    
    
    type: Literal["step"] = "step"
    
    

    model_config = ConfigDict(
        protected_namespaces=()
    )
import datetime
from typing import List, Optional, Dict, Union, Any, Literal
from uuid import UUID

from pydantic import BaseModel, Base64Bytes, AnyUrl, ConfigDict
from pydantic_extra_types.phone_numbers import PhoneNumber
from .base64data import Base64Data


from ..models.system import System


from ..models.selection import Selection


from ..models.stl_storage import StlStorage


from ..models.unit_length import UnitLength



class stl(BaseModel):
    """*ST**ereo**L**ithography format."""
    
    
    coords: System
    
    
    
    selection: Selection
    
    
    
    storage: StlStorage
    
    
    
    type: Literal["stl"] = "stl"
    
    
    
    units: UnitLength
    
    

    model_config = ConfigDict(
        protected_namespaces=()
    )
from typing import Dict, Any, Union, Type, TypeVar
from pydantic import RootModel, Field

from typing_extensions import Annotated




OutputFormat = RootModel[Annotated[Union[
        
        fbx,
        
        gltf,
        
        obj,
        
        ply,
        
        step,
        
        stl,
        
    ], Field(discriminator='type')]]

