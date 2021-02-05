rule __BJFnt_v1_3_nxptcn
{
	meta:
		description = "_BJFnt v1_3"
	strings:
		$a = {EB0305EB02EBFC55EB03EB0405EBFBEB53E80400000072}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
