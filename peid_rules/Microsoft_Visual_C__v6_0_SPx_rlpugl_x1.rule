rule _Microsoft_Visual_C__v6_0_SPx_rlpugl
{
	meta:
		description = "Microsoft Visual C__ v6_0 SPx"
	strings:
		$a = {558BEC83EC4456FF15????????6A018BF0FF15}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
