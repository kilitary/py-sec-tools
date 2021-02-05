rule _Microsoft_Visual_Basic_5_0_yqvgpz
{
	meta:
		description = "Microsoft Visual Basic 5_0"
	strings:
		$a = {FFFFFF0000000000003000000040000000000000}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
