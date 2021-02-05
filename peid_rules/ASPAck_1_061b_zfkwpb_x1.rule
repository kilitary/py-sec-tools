rule _ASPAck_1_061b_zfkwpb
{
	meta:
		description = "ASPAck 1_061b"
	strings:
		$a = {90907500E9}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
