rule _Microsoft_Visual_C__aayshs
{
	meta:
		description = "Microsoft Visual C__"
	strings:
		$a = {8B4424085683E8??74??4875}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
