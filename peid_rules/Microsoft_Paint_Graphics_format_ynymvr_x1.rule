rule _Microsoft_Paint_Graphics_format_ynymvr
{
	meta:
		description = "Microsoft Paint Graphics format"
	strings:
		$a = {4C696E53}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
