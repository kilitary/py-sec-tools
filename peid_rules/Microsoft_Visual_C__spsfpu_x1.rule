rule _Microsoft_Visual_C__spsfpu
{
	meta:
		description = "Microsoft Visual C__"
	strings:
		$a = {558BEC6AFF68????????68????????64A1000000005064892500000000}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
