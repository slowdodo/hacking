require 'msf/core'

class MetasploitModule < Msf::Exploit::Remote
  Rank = GreatRanking

  include Msf::Exploit::Remote::Tcp

  def initialize(info = {})
    super(update_info(info,
      'Name'           => 'Example Metasploit Module',
      'Description'    => %q{
        This is an example Metasploit module written in Ruby.
      },
      'Author'         => [ 'Your Name' ],
      'License'        => MSF_LICENSE,
      'References'     =>
        [
          [ 'URL', 'https://www.example.com' ],
        ],
      'Platform'       => 'linux',
      'Arch'           => [ ARCH_X86, ARCH_X86_64 ],
      'Payload'        =>
        {
          'BadChars' => "\x00\xff",
          'DisableNops' => true,
        },
      'Targets'        =>
        [
          [ 'Linux x86',
            {
              'Arch' => ARCH_X86,
              'Ret'  => 0x08041000,
            }
          ],
          [ 'Linux x86_64',
            {
              'Arch' => ARCH_X86_64,
              'Ret'  => 0x0000000000400000,
            }
          ],
        ],
      'DefaultTarget'  => 0,
      'DisclosureDate' => 'Jan 01 2000',
      'Privileged'     => false
    ))

    register_options(
      [
        Opt::RPORT(80),
        OptString.new('USERNAME', [ false, 'The username to authenticate with', '' ]),
        OptString.new('PASSWORD', [ false, 'The password to authenticate with', '' ])
      ], self.class)
  end

  def check
    connect
    res = sock.get_once(-1, 3)
    disconnect

    if res && res.include?('Server')
      return Exploit::CheckCode::Detected
    end

    Exploit::CheckCode::Safe
  end

  def exploit