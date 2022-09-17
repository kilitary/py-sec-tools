rule _PECompact_v1_33_ehhrrh
{
	meta:
		description = "PECompact v1_33"
	strings:
		$a = {EB0668????????C39C60E802??????33C08BC483C004938BE38B5BFC81EB0F8040??87DD8B85A28040??0185038040??66C785??8040??909001859E8040??BB2D12}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
