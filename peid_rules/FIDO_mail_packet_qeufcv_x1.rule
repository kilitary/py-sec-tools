rule _FIDO_mail_packet_qeufcv
{
	meta:
		description = "FIDO mail packet"
	strings:
		$a = {03000300CD07}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
