rule _Microsoft_Visual_C_2_0_ancbcp
{
	meta:
		description = "Microsoft Visual C 2_0"
	strings:
		$a = {64A100000000558BEC6AFF68}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
