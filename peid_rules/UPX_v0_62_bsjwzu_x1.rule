rule _UPX_v0_62_bsjwzu
{
	meta:
		description = "UPX v0_62"
	strings:
		$a = {807C2408010F859501000060E80000000058}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
