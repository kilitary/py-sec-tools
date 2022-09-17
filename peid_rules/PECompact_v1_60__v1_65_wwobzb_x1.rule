rule _PECompact_v1_60__v1_65_wwobzb
{
	meta:
		description = "PECompact v1_60 _ v1_65"
	strings:
		$a = {EB0668????????C39C60E802??????33C08BC483C004938BE38B5BFC81EB3F8040??87DD8B85D28040??0185338040??66C785??8040??90900185CE8040??BBBB12}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
