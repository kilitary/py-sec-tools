rule _PECompact_v1_33_qelqsp
{
	meta:
		description = "PECompact v1_33"
	strings:
		$a = {EB0668????????C39C60E802??????33C08BC483C004938BE38B5BFC81EB0F8040??87DD8B85A68040??0185038040??66C785008040??909001859E8040??BBE80E}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
