rule _Microsoft_Visual_C__8_gzalyq
{
	meta:
		description = "Microsoft Visual C__ 8"
	strings:
		$a = {E8????????E9}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
