rule _PCrypt_v3_51_saxrel
{
	meta:
		description = "PCrypt v3_51"
	strings:
		$a = {504352595054FF76332E353100E9}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
