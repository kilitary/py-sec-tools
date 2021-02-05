rule _PECompact_v0_978_ewboop
{
	meta:
		description = "PECompact v0_978"
	strings:
		$a = {EB0668????????C39C60E802??????33C08BC483C004938BE38B5BFC81EBD18440??87DD8B855685}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
