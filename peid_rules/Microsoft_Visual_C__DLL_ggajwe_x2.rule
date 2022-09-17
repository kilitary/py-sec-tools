rule _Microsoft_Visual_C__DLL_ggajwe
{
	meta:
		description = "Microsoft Visual C__ DLL"
	strings:
		$a = {558BEC5657BF010000008B750C}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
