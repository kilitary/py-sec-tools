rule _Armadillo_4_40__Silicon_Realms_Toolworks_lvifhg
{
	meta:
		description = "Armadillo 4_40 __ Silicon Realms Toolworks"
	strings:
		$a = {312E312E34000000C2E094BE93FCDEC6B62483F7D2A492774027CFEBD86F50B4B52924FA45080452D51BD28C8A1E6EFF8C5F4289F183B127C56957FC550ADD44BE2A02976B6515AA31E9287D491BDFB55D08A8BAA8}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
