rule _Microsoft_Visual_C_2_0_tjbmlz
{
	meta:
		description = "Microsoft Visual C 2_0"
	strings:
		$a = {535657BB????????8B??????553BFB75}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
