rule _CERBERUS_v2_0_onmprg
{
	meta:
		description = "CERBERUS v2_0"
	strings:
		$a = {9C2BED8C????8C????FAE4??88????1607BF????8EDD9BF5B9????FCF3A5}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
