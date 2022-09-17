rule _Microsoft_Visual_C__7_0_jzmukw
{
	meta:
		description = "Microsoft Visual C__ 7_0"
	strings:
		$a = {6A0C68????????E8????????33C0408945E48B750C}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
