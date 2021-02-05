rule _PECompact_v0_978_2_emlrnc
{
	meta:
		description = "PECompact v0_978_2"
	strings:
		$a = {EB0668????????C39C60E802??????33C08BC483C004938BE38B5BFC81EBC48440??87DD8B854985}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
