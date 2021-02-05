rule _Simple_UPX_Cryptor_v30_4_2005_multi_layer_encryption_gckuuu
{
	meta:
		description = "Simple UPX Cryptor v30_4_2005 _multi layer encryption"
	strings:
		$a = {60B8????????B918000000803408??E2FA6168????????C3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
