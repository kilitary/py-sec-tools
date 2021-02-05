rule _Microsoft_Visual_C__8_0_xvvlie
{
	meta:
		description = "Microsoft Visual C__ 8_0"
	strings:
		$a = {6A0C68????????E8????????33C0408945E4}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
