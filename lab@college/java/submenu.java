
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.KeyEvent;

import javax.swing.ImageIcon;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JMenu;
import javax.swing.JMenuBar;
import javax.swing.JMenuItem;
import javax.swing.KeyStroke;
import javax.swing.SwingUtilities;


public class submenu extends JFrame {

    public submenu() {
        initUI();
    }

    public final void initUI() {
	
	JPanel panel = new JPanel();
       getContentPane().add(panel);

       panel.setLayout(null);

       JButton quitButton = new JButton("Quit");
       quitButton.setBounds(320, 430, 80, 30);
       quitButton.setToolTipText("Click this button to exit the window");
       quitButton.addActionListener(new ActionListener() {
           public void actionPerformed(ActionEvent event) {
               System.exit(0);
          }
       });

	
        JMenuBar menubar = new JMenuBar();
        ImageIcon iconNew = new ImageIcon(getClass().getResource("new.png"));
        ImageIcon iconOpen = new ImageIcon(getClass().getResource("open.png"));
        ImageIcon iconSave = new ImageIcon(getClass().getResource("save.png"));
        ImageIcon iconExit = new ImageIcon(getClass().getResource("exit.png"));
//Now the label
	ImageIcon iconLabel = new ImageIcon(getClass().getResource("icon.png"));
	JLabel label=new JLabel(iconLabel);
	label.setBounds(280,130,180,230);
//Now the submenu 
	JLabel label2=new JLabel("arcolife");
	label2.setBounds(350,130,50,550);

        JMenu file = new JMenu("File");
        file.setMnemonic(KeyEvent.VK_F);

        JMenu imp = new JMenu("Import");
        imp.setMnemonic(KeyEvent.VK_M);

        JMenuItem newsf = new JMenuItem("Import newsfeed list...");
        JMenuItem bookm = new JMenuItem("Import bookmarks...");
        JMenuItem mail = new JMenuItem("Import mail...");

        imp.add(newsf);
        imp.add(bookm);
        imp.add(mail);

        JMenuItem fileNew = new JMenuItem(iconNew);
        fileNew.setMnemonic(KeyEvent.VK_N);

        JMenuItem fileOpen = new JMenuItem(iconOpen);
        fileNew.setMnemonic(KeyEvent.VK_O);

        JMenuItem fileSave = new JMenuItem(iconSave);
        fileSave.setMnemonic(KeyEvent.VK_S);

        JMenuItem fileExit = new JMenuItem(iconExit);
        fileExit.setMnemonic(KeyEvent.VK_C);
        fileExit.setToolTipText("Exit application");
        fileExit.setAccelerator(KeyStroke.getKeyStroke(KeyEvent.VK_W,
            ActionEvent.CTRL_MASK));

        fileExit.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent event) {
                System.exit(0);
            }

        });

        file.add(fileNew);
        file.add(fileOpen);
        file.add(fileSave);
        file.addSeparator();
        file.add(imp);
        file.addSeparator();
        file.add(fileExit);

        menubar.add(file);

	panel.add(quitButton);
	panel.add(label);
        panel.add(label2);
	setJMenuBar(menubar);

        setTitle("MultiFunctional JFrame app");
        setSize(720, 550);
        setLocationRelativeTo(null);
        setDefaultCloseOperation(EXIT_ON_CLOSE);
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(new Runnable() {
            public void run() {
                submenu ex = new submenu();
                ex.setVisible(true);
            }
        });
    }
}