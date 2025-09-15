import {
  Streamlit,
  StreamlitComponentBase,
  withStreamlitConnection,
} from "streamlit-component-lib";
import React from "react";
import { style } from "glamor";
import "./component.css";
import "./icons/icon.css";

class SideNav extends StreamlitComponentBase {
  constructor(props) {
    super(props);
    this.state = { openParentIndex: null };
  }

  handleParentClick = (parent, index) => {
    if (parent.children && parent.children.length > 0) {
      this.setState((prev) => ({
        openParentIndex: prev.openParentIndex === index ? null : index,
      }));
    } else {
      Streamlit.setComponentValue(parent.label);
    }
  };

  handleChildClick = (child) => {
    Streamlit.setComponentValue(child.label);
  };

  render = () => {
    const menuData = this.props.args["menuData"] || [];
    const styles = this.props.args["styles"] || {};
    const { openParentIndex } = this.state;

    return (
      <div className="navtab" {...style(styles["navtab"]) }>
        <ul className="all-tabs-options">
          {menuData.map((parent, index) => (
            <li
              className="tab-container"
              {...style(styles["tabOptionsStyle"])}
              key={`parent-${index}`}
            >
              <div
                className="tab"
                {...style(styles["tabStyle"])}
                onClick={() => this.handleParentClick(parent, index)}
              >
                <i className="material-icons" {...style(styles["iconStyle"]) }>
                  {parent.icon}
                </i>
                <span className="labelName">{parent.label}</span>
              </div>
              {parent.children && openParentIndex === index && (
                <ul className="child-tabs">
                  {parent.children.map((child, cIndex) => (
                    <li
                      className="child-tab"
                      {...style(styles["tabStyle"])}
                      onClick={() => this.handleChildClick(child)}
                      key={`child-${index}-${cIndex}`}
                    >
                      <i
                        className="material-icons"
                        {...style(styles["iconStyle"])}
                      >
                        {child.icon}
                      </i>
                      <span className="labelName">{child.label}</span>
                    </li>
                  ))}
                </ul>
              )}
            </li>
          ))}
        </ul>
      </div>
    );
  };
}

export default withStreamlitConnection(SideNav);

