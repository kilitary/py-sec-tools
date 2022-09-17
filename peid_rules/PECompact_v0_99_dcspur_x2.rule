rule _PECompact_v0_99_dcspur
{
	meta:
		description = "PECompact v0_99"
	strings:
		$a = {EB0668????????C39C60E802??????33C08BC483C004938BE38B5BFC81EB286340??87DD8B85AD63}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
