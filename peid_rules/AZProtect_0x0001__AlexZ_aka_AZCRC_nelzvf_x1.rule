rule _AZProtect_0x0001__AlexZ_aka_AZCRC_nelzvf
{
	meta:
		description = "AZProtect 0x0001 __ AlexZ aka AZCRC"
	strings:
		$a = {EB70FC608C804D110070258100400D91BB608C804D11007021811D610D810040CE608C804D11007025812581258125812961418131611D610040B7300000}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
