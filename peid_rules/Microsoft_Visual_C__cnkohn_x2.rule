rule _Microsoft_Visual_C__cnkohn
{
	meta:
		description = "Microsoft Visual C__"
	strings:
		$a = {558BEC5657BF????????8B????3BF70F}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
