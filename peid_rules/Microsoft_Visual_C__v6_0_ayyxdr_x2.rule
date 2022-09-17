rule _Microsoft_Visual_C__v6_0_ayyxdr
{
	meta:
		description = "Microsoft Visual C__ v6_0"
	strings:
		$a = {558BEC83EC4456FF15????????8BF08A??3C22}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
