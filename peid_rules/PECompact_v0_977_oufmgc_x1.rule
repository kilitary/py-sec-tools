rule _PECompact_v0_977_oufmgc
{
	meta:
		description = "PECompact v0_977"
	strings:
		$a = {EB0668????????C39C60E802??????33C08BC483C004938BE38B5BFC81EBA08640??87DD8B852A87}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
