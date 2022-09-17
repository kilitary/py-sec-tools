rule _VX_TibsZhelatin_StormWorm_variant_enpywa
{
	meta:
		description = "VX_ TibsZhelatin _StormWorm_ variant"
	strings:
		$a = {FF74241C588D80????7704506862343504E8}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
