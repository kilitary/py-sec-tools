rule _Microsoft_Visual_C__nnynfs
{
	meta:
		description = "Microsoft Visual C__"
	strings:
		$a = {8B44240883????74}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
