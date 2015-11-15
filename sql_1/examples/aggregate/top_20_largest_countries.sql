select Name, max(SurfaceArea)
from Country
order by SurfaceArea desc
limit 20;
