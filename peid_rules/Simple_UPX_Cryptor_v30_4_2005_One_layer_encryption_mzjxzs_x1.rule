rule _Simple_UPX_Cryptor_v30_4_2005_One_layer_encryption_mzjxzs
{
	meta:
		description = "Simple UPX Cryptor v30_4_2005 _One layer encryption"
	strings:
		$a = {60B8??????00B9??010000803408??E2FA6168??????00C3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
