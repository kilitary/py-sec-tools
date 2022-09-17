rule _PECompact_v1_22_ekujkg
{
	meta:
		description = "PECompact v1_22"
	strings:
		$a = {EB0668????????C39C60E802??????33C08BC483C004938BE38B5BFC81EB0F7040??87DD8B85A67040??0185037040??66C785??7040??909001859E7040??BBF308}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
